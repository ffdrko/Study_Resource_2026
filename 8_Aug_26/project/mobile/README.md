# 📱 SnapNote Mobile (React Native + Expo)

Mobile client for the SnapNote OCR API. Photograph your notes, extract text, and share a formatted `.docx`.

## Prerequisites

1. **SnapNote server running** on your computer:
   ```
   cd ../server
   node index.js
   ```
2. **Expo Go app** installed on your phone ([Android](https://play.google.com/store/apps/details?id=host.exp.exponent) / [iOS](https://apps.apple.com/app/expo-go/id982107779))

## Setup

```bash
cd mobile
npm install
```

### ⚠️ Configure the API URL (required for real phones)

Open `api.js` and set `API_URL` to your **computer's local IP**:

```js
export const API_URL = 'http://192.168.1.XX:3000'; // find with `ipconfig`
```

- **Android emulator:** `http://10.0.2.2:3000` works automatically
- **Real phone:** must use LAN IP, and phone + PC must be on the same Wi-Fi

## Run

```bash
npx expo start
```

Scan the QR code with the Expo Go app (Android) or Camera app (iOS).

## Features

- 📷 Camera capture or gallery multi-select
- 🔍 Sequential OCR with progress status
- ✏️ Editable extracted text before formatting
- 👁 Live preview of headings/bullets/bold
- ⬇️ Export `.docx` → native share sheet (save to Files, send via email/WhatsApp, etc.)

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Network request failed | Check API_URL matches PC's IP; same Wi-Fi network |
| Windows Firewall blocks it | Allow inbound port 3000 for Node.js |
| Camera permission denied | Re-enable in phone Settings → Expo Go |
