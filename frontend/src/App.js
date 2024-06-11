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
import { UserProvider } from "./provider/UserStateProvider";
import { ScreenStateProvider } from "./provider/ScreenStateProvider";

function App() {


  return (
    <GoogleOAuthProvider clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}>
      <Router>
        <GlobalStateProvider>
          <ScreenStateProvider>
            <UserProvider>
              <MessageStateProvider>
                <div className="App">
                  <Routes>
                    <Route path="/" element={<Home />} />
                  </Routes>
                </div>
              </MessageStateProvider>
            </UserProvider>
          </ScreenStateProvider>
        </GlobalStateProvider>
      </Router>
    </GoogleOAuthProvider>
  );
}

export default App;
