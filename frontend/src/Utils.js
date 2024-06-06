export const States = {
  WAITING_FOR_MESSAGE: "waiting_for_message",
  PROCESSING_MESSAGE: "processing_message",
  ERROR: "error",
};

export const STATE_HINTS = {
  waiting_for_message: "Please Enter your initial prompt.",
  processing_message: "Processing message.",
  error: "Error",
};

export const BASE_URL = "http://localhost:8000/api/v1/";
export const ENDPOINTS = {};

export const AUTHOR = {
  AI: "AI",
  USER: "user",
};
