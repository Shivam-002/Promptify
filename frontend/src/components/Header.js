import React, { useEffect, useState } from "react";

import { Avatar, message, Switch } from "antd";
import { BugOutlined, GoogleOutlined } from "@ant-design/icons";

import "./../css/Header.css";
import { useGlobalStateContext } from "../provider/GlobalStateProvider";
import PromptifyLogo from "./PromptifyLogo";
import { GoogleLogin } from "@react-oauth/google";

function Header() {
  const { activeState, handleGlobalStateChange } = useGlobalStateContext();

  const onDebugModeChange = (checked) => {
    message.info(`Debug Mode ${checked ? "Activated" : "Deactivated"}!`);

    handleGlobalStateChange({
      ...activeState,
      debugMode: checked,
    });
  };

  const onGoogleLoginSuccess = (response) => {
    message.success("Google Login Successful!");
    const token = response.credential;
    localStorage.setItem("token", token);
  };

  const onGoogleLoginError = (error) => {
    message.error("Google Login Failed!");
  };

  useEffect(() => {
    console.log(document.cookie);
  }, []);

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
        <GoogleLogin
          onSuccess={onGoogleLoginSuccess}
          onError={onGoogleLoginError}
          useOneTap
          auto_select
        />
        ;
        {/* <Avatar
          style={{
            backgroundColor: "#f56a00",
            verticalAlign: "middle",
          }}
          size="large"
          gap={1}
        >
          {"S"}
        </Avatar> */}
      </div>
    </div>
  );
}

export default Header;
