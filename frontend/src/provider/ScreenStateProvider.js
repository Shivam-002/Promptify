import { createContext, useContext, useState } from "react";
import { States } from "../Utils";

const ScreenStateContext = createContext();

export const useScreenStateContext = () => useContext(ScreenStateContext);

export const ScreenStateProvider = ({ children }) => {
  const [screenState, setScreenState] = useState({
    isMobile: false,
  });

  const handleScreenStateChange = (screenState) => {
    setScreenState(screenState);
  };

  return (
    <ScreenStateContext.Provider
      value={{ screenState, handleScreenStateChange }}
    >
      {children}
    </ScreenStateContext.Provider>
  );
};
