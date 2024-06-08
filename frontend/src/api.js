import axios from "axios";
import { ENDPOINTS } from "./Utils";

const get_auth_header = () => {
  console.log("token", localStorage.getItem("token"));
  return {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  };
};

export const query = async (input_prompt, context, on_succes, on_failure) => {
  axios.interceptors.request.use((request) => {
    console.log("Starting Request", JSON.stringify(request, null, 2));
    return request;
  });
  const endpoint = `${ENDPOINTS.QUERY}?input_prompt=${input_prompt}&context=${context}`;
  await axios.get(endpoint, get_auth_header()).then(
    (response) => {
      on_succes(response);
    },
    (error) => {
      on_failure(error);
    }
  );
};

export const authenticate = async (access_token, on_succes, on_failure) => {
  try {
    const endpoint = `${ENDPOINTS.LOGIN}?access_token=${access_token}`;
    const response = await axios.get(endpoint);
    on_succes(response);
  } catch (error) {
    on_failure(error);
  }
};

export const test = async (on_succes, on_failure) => {
  try {
    const endpoint = `${ENDPOINTS.TEST}`;
    const response = await axios.get(endpoint, get_auth_header());
    on_succes(response);
  } catch (error) {
    on_failure(error);
  }
};
