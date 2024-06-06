import React from "react";

import { Avatar, message, Switch } from "antd";
import { BugOutlined } from "@ant-design/icons";

import "./../css/Header.css";
import { useGlobalStateContext } from "../provider/GlobalStateProvider";
import PromptifyLogo from "./PromptifyLogo";

function Header() {
  const { activeState, handleGlobalStateChange } = useGlobalStateContext();

  const onDebugModeChange = (checked) => {
    message.info(`Debug Mode ${checked ? "Activated" : "Deactivated"}!`);

    handleGlobalStateChange({
      ...activeState,
      debugMode: checked,
    });
  };

  return (
    <div className="header-container">
      <PromptifyLogo />

      <div className="menu-container">
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
            justifyContent: "center",
            gap: "10px",
          }}
        >
          <BugOutlined
            style={{
              color: activeState.debugMode ? "green" : "black",
              opacity: activeState.debugMode ? 1 : 0.5,
              fontSize: "25px",
            }}
          />
          <Switch onChange={onDebugModeChange} />
        </div>
        <Avatar
          style={{
            backgroundColor: "#f56a00",
            verticalAlign: "middle",
          }}
          size="large"
          gap={1}
        >
          {"S"}
        </Avatar>
      </div>
    </div>
  );
}

export default Header;
