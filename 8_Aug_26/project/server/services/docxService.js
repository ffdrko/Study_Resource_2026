const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  HeadingLevel,
} = require('docx');

const HEADING_MAP = {
  heading1: HeadingLevel.HEADING_1,
  heading2: HeadingLevel.HEADING_2,
  heading3: HeadingLevel.HEADING_3,
};

function runsFrom(block) {
  if (block.text !== undefined) {
    return [new TextRun({ text: block.text })];
  }
  return (block.runs || []).map(
    (r) => new TextRun({ text: r.text, bold: !!r.bold, italics: !!r.italic })
  );
}

/**
 * @param {Array<object>} blocks - structured blocks from formatService
 * @param {string} title
 * @returns {Promise<Buffer>} docx file buffer
 */
async function buildDocx(blocks, title) {
  const children = [
    new Paragraph({ text: title, heading: HeadingLevel.TITLE }),
  ];

  for (const block of blocks) {
    if (HEADING_MAP[block.type]) {
      children.push(new Paragraph({ heading: HEADING_MAP[block.type], children: runsFrom(block) }));
    } else if (block.type === 'bullet') {
      children.push(new Paragraph({ bullet: { level: 0 }, children: runsFrom(block) }));
    } else if (block.type === 'numbered') {
      children.push(new Paragraph({ numbering: { reference: 'snapnote-numbered', level: 0 }, children: runsFrom(block) }));
    } else {
      children.push(new Paragraph({ children: runsFrom(block) }));
    }
  }

  const doc = new Document({
    numbering: {
      config: [
        {
          reference: 'snapnote-numbered',
          levels: [
            {
              level: 0,
              format: 'decimal',
              text: '%1.',
              alignment: 'start',
              style: { paragraph: { indent: { left: 720, hanging: 360 } } },
            },
          ],
        },
      ],
    },
    sections: [{ children }],
  });

  return Packer.toBuffer(doc);
}

module.exports = { buildDocx };
