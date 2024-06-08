import "./App.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import Home from "./pages/Home";

import { GlobalStateProvider } from "./provider/GlobalStateProvider";
import { MessageStateProvider } from "./provider/MessageStateProvider";

import { GoogleOAuthProvider } from "@react-oauth/google";

function App() {
  console.log(process.env.REACT_APP_GOOGLE_CLIENT_ID);

  return (
    <GoogleOAuthProvider clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}>
      <Router>
        <GlobalStateProvider>
          <MessageStateProvider>
            <div className="App">
              <Routes>
                <Route path="/" element={<Home />} />
              </Routes>
            </div>
          </MessageStateProvider>
        </GlobalStateProvider>
      </Router>
    </GoogleOAuthProvider>
  );
}

export default App;
