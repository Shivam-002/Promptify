import React, { memo, useEffect, useState } from "react";
import PromptTemplate from "./PromptTemplate";
import { AUTHOR, PROMPT_TEMPLATE, States } from "../Utils";
import { useGlobalStateContext } from "../provider/GlobalStateProvider";
import { useMessageContext } from "../provider/MessageStateProvider";
import { query } from "../api";
import { message } from "antd";

import "./../css/PromptTemplateGroup.css";

const PromptTemplateGroup = memo(() => {
  const { activeState, handleGlobalStateChange } = useGlobalStateContext();
  const { messages, handleMessagesChange } = useMessageContext();

  const [template_prompts, setTemplatePrompts] = useState([]);

  useEffect(() => {
    const shuffledPrompts = [...PROMPT_TEMPLATE]
      .sort(() => 0.5 - Math.random())
      .slice(0, 3);
    setTemplatePrompts(shuffledPrompts);
  }, []);

  return (
    <div className="prompt-template-group">
      {template_prompts.map((template) => (
        <PromptTemplate
          key={template.id}
          title={template.title}
          prompt={template.prompt}
          icon={template.icon}
          onClick={() => {
            handleGlobalStateChange((prevState) => ({
              ...prevState,
              state: States.PROCESSING_MESSAGE,
            }));

            handleMessagesChange((prevState) => [
              ...prevState,
              {
                author: AUTHOR.USER,
                text: template.prompt,
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
                message.error(
                  "Failed to query the model. Please try again later."
                );
                console.error("query failed : ", error);
                handleGlobalStateChange((prevState) => ({
                  ...prevState,
                  state: States.WAITING_FOR_MESSAGE,
                }));
              }
            );
          }}
        />
      ))}
    </div>
  );
});

export default PromptTemplateGroup;
