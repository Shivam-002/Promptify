import React, { useEffect } from "react";
import Header from "../components/Header";
import Body from "../components/Body";
import { useScreenStateContext } from "../provider/ScreenStateProvider";

function Home() {
  const { screenState, handleScreenStateChange } = useScreenStateContext();

  useEffect(() => {
    const handleResize = () => {
      const isMobile = window.innerWidth < 768;
      handleScreenStateChange((prevState) => ({
        ...prevState,
        isMobile: isMobile,
      }));
    };

    console.log("screen state : ", screenState);

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, [handleScreenStateChange]);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100vh",
        width: "100vw",
      }}
    >
      <Header />
      <Body />
    </div>
  );
}

export default Home;
