import React, { useState } from "react";
import MessageBox from "./MessageBox";

import "./../css/Chat.css";
import { useMessageContext } from "../provider/MessageStateProvider";
import { useGlobalStateContext } from "../provider/GlobalStateProvider";
import PromptTemplateGroup from "./PromptTemplateGroup";
import { States } from "../Utils";
function Chat() {
  const { activeState, handleGlobalStateChange } = useGlobalStateContext();

  const { messages, handleMessagesChange } = useMessageContext();
  return (
    <div
      className="chat-container"
      style={{
        justifyContent: messages.length > 0 ? "flex-start" : "center",
      }}
    >
      {messages.length > 0 ? (
        messages.map((message, index) => (
          <MessageBox
            key={index}
            author={message.author}
            input_message={message.text}
          />
        ))
      ) : (
        <PromptTemplateGroup />
      )}
      {activeState.state === States.PROCESSING_MESSAGE && (
        <MessageBox author="AI" input_message={""} is_skeleton={true} />
      )}
    </div>
  );
}

export default Chat;
