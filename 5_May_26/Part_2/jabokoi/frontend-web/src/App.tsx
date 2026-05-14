import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

// Placeholder components
const Home = () => <div className="p-8 text-2xl font-bold">Jabo Koi Home</div>;
const Login = () => <div className="p-8">Login Page</div>;
const Register = () => <div className="p-8">Register Page</div>;
const Chat = () => <div className="p-8">Chat Interface</div>;
const PlanView = () => <div className="p-8">Trip Plan View</div>;

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/plan/:id" element={<PlanView />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
