import React from "react";
import { Avatar, Tooltip, message } from "antd";
import { CopyOutlined, RedoOutlined } from "@ant-design/icons";
import "./../css/MessageBox.css";
import ReactMarkdown from "react-markdown";
import { AUTHOR, States } from "../Utils";
import { useGlobalStateContext } from "../provider/GlobalStateProvider";
import { useMessageContext } from "../provider/MessageStateProvider";
import { query } from "../api";
function MessageBox({ author, input_message }) {
  const copyToClipboard = () => {
    navigator.clipboard.writeText(input_message);
    message.success("Copied to clipboard!");
  };

  const { activeState, handleGlobalStateChange } = useGlobalStateContext();
  const { messages, handleMessagesChange } = useMessageContext();

  const queryQuestion = () => {};
  const regenerate = () => {
    handleGlobalStateChange((prevState) => ({
      ...prevState,
      state: States.PROCESSING_MESSAGE,
      lastMessage: input_message,
    }));

    handleMessagesChange((prevState) => [
      ...prevState,
      {
        author: AUTHOR.USER,
        text: input_message,
      },
    ]);
    //TODO : query
  };

  return (
    <div className="message-box">
      {author === "AI" ? (
        <Avatar size={50} className="ai-avatar">
          AI
        </Avatar>
      ) : (
        <svg
          width="50"
          height="49"
          viewBox="0 0 37 36"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          //TODO : SVG LOGO
        </svg>
      )}

      <div className="message-content">
        <ReactMarkdown className="message-text">{input_message}</ReactMarkdown>
        <div className="icon-container">
          {input_message && (
            <Tooltip title="Copy">
              <CopyOutlined className="quick-icon" onClick={copyToClipboard} />
            </Tooltip>
          )}
          {author !== "AI" && (
            <Tooltip title="Regenerate">
              <RedoOutlined
                className={`quick-icon ${
                  activeState.state === States.PROCESSING_MESSAGE
                    ? "disable-quick-icon"
                    : ""
                }`}
                onClick={
                  activeState.state === States.PROCESSING_MESSAGE
                    ? null
                    : regenerate
                }
              />
            </Tooltip>
          )}
        </div>
      </div>
    </div>
  );
}

export default MessageBox;
