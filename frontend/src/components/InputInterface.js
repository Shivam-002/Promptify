import React from "react";
import { Button, Tooltip, message } from "antd";
import { SendOutlined, LoadingOutlined } from "@ant-design/icons";

import "./../css/InputInterface.css";
import { useGlobalStateContext } from "../provider/GlobalStateProvider";
import { AUTHOR, States } from "../Utils";
import TextArea from "antd/es/input/TextArea";
import { useMessageContext } from "../provider/MessageStateProvider";
import { query } from "../api";

function InputInterface() {
  const { activeState, handleGlobalStateChange } = useGlobalStateContext();
  const { messages, handleMessagesChange } = useMessageContext();

  const onMessageChanged = (e) => {
    handleGlobalStateChange((prevState) => ({
      ...prevState,
      lastMessage: e.target.value,
    }));
  };

  const queryQuestion = () => {
    if (!activeState.lastMessage || activeState.lastMessage.trim() === "") {
      return;
    }

    handleGlobalStateChange((prevState) => ({
      ...prevState,
      state: States.PROCESSING_MESSAGE,
    }));

    handleMessagesChange((prevState) => [
      ...prevState,
      {
        author: AUTHOR.USER,
        text: activeState.lastMessage,
      },
    ]);
    query(
      activeState.lastMessage,
      null,
      (res) => {
        handleMessagesChange((prevState) => [
          ...prevState,
          {
            author: AUTHOR.AI,
            text: res.data,
          },
        ]);
        handleGlobalStateChange((prevState) => ({
          ...prevState,
          state: States.WAITING_FOR_MESSAGE,
        }));
      },
      (error) => {
        message.error("Failed to query the model. Please try again later.");
        handleGlobalStateChange((prevState) => ({
          ...prevState,
          state: States.WAITING_FOR_MESSAGE,
        }));
      }
    );
  };

  return (
    <div className="input-interface-container">
      <TextArea
        variant="borderless"
        placeholder="Send a message..."
        onChange={onMessageChanged}
        style={{
          overflowX: "auto",
        }}
        autoSize={{ minRows: 1, maxRows: 6 }}
      />
      {activeState.state === States.PROCESSING_MESSAGE ? (
        <Tooltip title="Processing">
          <LoadingOutlined />
        </Tooltip>
      ) : (
        <Tooltip title="Send Message">
          <Button
            style={{
              backgroundColor: "transparent",
              borderRadius: "20%",
              border: "none",
              boxShadow: "none",
            }}
            icon={<SendOutlined />}
            className={
              !message || activeState.state !== States.WAITING_FOR_MESSAGE
                ? "disabled-send-btn"
                : "active-send-btn"
            }
            onClick={
              !message || activeState.state !== States.WAITING_FOR_MESSAGE
                ? null
                : queryQuestion
            }
          ></Button>
        </Tooltip>
      )}
    </div>
  );
}

export default InputInterface;
