import React from "react";
import "./../css/PromptTemplate.css";
import { Card } from "antd";
import { motion } from "framer-motion";

function PromptTemplate({ icon, title, prompt, onClick }) {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{
        type: "spring",
        stiffness: 160,
        damping: 30,
      }}
    >
      <Card
        title={title}
        extra={
          icon ? <img src={icon} alt="icon" className="prompt-icon" /> : null
        }
        className="prompt-template"
        onClick={onClick}
      >
        <p>{prompt}</p>
      </Card>
    </motion.div>
  );
}

export default PromptTemplate;
