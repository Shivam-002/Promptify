import React, { useEffect, useState } from "react";

import { Avatar, message, Switch } from "antd";
import { BugOutlined, GoogleOutlined } from "@ant-design/icons";

import "./../css/Header.css";
import { useGlobalStateContext } from "../provider/GlobalStateProvider";
import PromptifyLogo from "./PromptifyLogo";
import { GoogleLogin } from "@react-oauth/google";
import { useUserContext } from "../provider/UserStateProvider";

import { jwtDecode } from "jwt-decode";
import { useScreenStateContext } from "../provider/ScreenStateProvider";

function Header() {
  const { activeState, handleGlobalStateChange } = useGlobalStateContext();
  const { user, handleUserChange } = useUserContext();
  const { screenState, handleScreenStateChange } = useScreenStateContext();
  const onGoogleLoginSuccess = (response) => {
    const token = response.credential;

    const decoded = jwtDecode(token);

    const { name, email, picture } = decoded;
    handleUserChange({
      name: name,
      email: email,
      picture_url: picture,
    });

    message.success(`Welcome ${name}!`);
    localStorage.setItem("token", token);
  };

  const fetchUser = () => {
    const token = localStorage.getItem("token");
    if (token) {
      console.log("Token found in local storage", token);
      const decoded = jwtDecode(token);
      const { name, email, picture } = decoded;
      console.log("Decoded", decoded);
      handleUserChange({
        name: name,
        email: email,
        picture_url: picture,
      });
    }
  };

  useEffect(() => {
    fetchUser();
  }, []);

  const onGoogleLoginError = (error) => {
    message.error("Google Login Failed!");
  };

  return (
    <div className="header-container">
      <PromptifyLogo />

      <div className="menu-container">
        <GoogleLogin
          onSuccess={onGoogleLoginSuccess}
          onError={onGoogleLoginError}
          auto_select
          shape="circle"
          type={screenState.isMobile ? "icon" : "standard"}
        />
      </div>
    </div>
  );
}

export default Header;
