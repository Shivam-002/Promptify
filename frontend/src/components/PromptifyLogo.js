import React, { useEffect, useState } from "react";
import { ReactTyped } from "react-typed";
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
      <h1
        style={{
          color: "black",
        }}
      >
        <strong>
          <ReactTyped
            strings={["Welcome to Promptify"]}
            typeSpeed={50}
            showCursor={false}
          />
        </strong>
      </h1>
    </div>
  );
}

export default PromptifyLogo;
