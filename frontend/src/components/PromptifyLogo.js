import React, { useEffect, useState } from "react";
import { ReactTyped } from "react-typed";
import "./../css/PromptifyLogo.css";
function PromptifyLogo() {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <ReactTyped
        strings={["Welcome to Promptify!"]}
        typeSpeed={50}
        showCursor={false}
        className="promptify-logo"
        style={{
          fontFamily: "Rubik",
          color: "#000",
          fontWeight: "bold",
        }}
      />
    </div>
  );
}

export default PromptifyLogo;
  