import axios from "axios";
import { ENDPOINTS } from "./Utils";

export const query = async (input_prompt, context, on_succes, on_failure) => {
  try {
    const endpoint = `${ENDPOINTS.QUERY}/?input_prompt=${input_prompt}&context=${context}`;
    const response = await axios.get(endpoint, {
      input_prompt: input_prompt,
      context: context,
    });
    on_succes(response);
  } catch (error) {
    on_failure(error);
  }
};
