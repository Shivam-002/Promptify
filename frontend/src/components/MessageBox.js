import React from "react";
import { Avatar, Skeleton, Tooltip, message } from "antd";
import { CopyOutlined, RedoOutlined } from "@ant-design/icons";
import "./../css/MessageBox.css";
import ReactMarkdown from "react-markdown";
import { AUTHOR, States } from "../Utils";
import { useGlobalStateContext } from "../provider/GlobalStateProvider";
import { useMessageContext } from "../provider/MessageStateProvider";
import { query } from "../api";
import { useUserContext } from "../provider/UserStateProvider";
function MessageBox({ author, input_message, is_skeleton }) {
  const copyToClipboard = () => {
    navigator.clipboard.writeText(input_message);
    message.success("Copied to clipboard!");
  };

  const { activeState, handleGlobalStateChange } = useGlobalStateContext();
  const { messages, handleMessagesChange } = useMessageContext();
  const { user, handleUserChange } = useUserContext();

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
        <Avatar className="ai-avatar">AI</Avatar>
      ) : user.picture_url ? (
        <img
          className="user-img"
          src={user.picture_url}
          alt="User Profile Photo"
        />
      ) : (
        <Avatar className="user-avatar">
          {user.name ? user.name[0] : "U"}
        </Avatar>
      )}

      {!is_skeleton ? (
        <div className="message-content">
          <ReactMarkdown className="message-text">
            {input_message}
          </ReactMarkdown>
          <div className="icon-container">
            {input_message && (
              <Tooltip title="Copy">
                <CopyOutlined
                  className="quick-icon"
                  onClick={copyToClipboard}
                />
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
      ) : (
        <Skeleton active paragraph={{ rows: 3 }} />
      )}
    </div>
  );
}

export default MessageBox;
