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
export const ENDPOINTS = {
  QUERY: `${BASE_URL}query`,
  LOGIN: `${BASE_URL}auth/google`,
  TEST: `${BASE_URL}test`,
};

export const AUTHOR = {
  AI: "AI",
  USER: "user",
};

export const PROMPT_TEMPLATE = [
  {
    id: 1,
    title: "Recipe ",
    prompt:
      "Write a prompt to generate a detailed recipe for making homemade lasagna, including a list of ingredients, step-by-step instructions, and cooking tips.",
    icon: "./prompt_template_icons/recipe.png",
  },
  {
    id: 2,
    title: "Travel Guide ",
    prompt:
      "Write a prompt to generate a detailed travel guide about the top attractions and hidden gems in Tokyo, Japan.",
    icon: "./prompt_template_icons/tourism.png",
  },
  {
    id: 3,
    title: "Tech Review ",
    prompt:
      "Write a prompt to generate an in-depth review of the latest iPhone model, including its features, performance, and comparison with previous models.",
    icon: "./prompt_template_icons/tech_guide.png",
  },
  {
    id: 4,
    title: "Fitness Guide ",
    prompt:
      "Write a prompt to generate a comprehensive guide on starting a beginner's workout routine, including exercises, schedules, and nutritional advice.",
    icon: "./prompt_template_icons/fitness_guide.png",
  },
  {
    id: 5,
    title: "Historical Article ",
    prompt:
      "Write a prompt to generate a detailed article about the causes and consequences of the French Revolution.",
    icon: "./prompt_template_icons/mythical.png",
  },
  {
    id: 6,
    title: "Product Description ",
    prompt:
      "Write a prompt to generate a detailed product description for a new line of eco-friendly, reusable water bottles, highlighting their benefits and unique features.",
    icon: "./prompt_template_icons/product_description.png",
  },
  {
    id: 7,
    title: "Science Explainer ",
    prompt:
      "Write a prompt to generate a detailed explanation of how quantum computers work and their potential impact on various industries.",
    icon: "./prompt_template_icons/science.png",
  },
  {
    id: 8,
    title: "Business Plan ",
    prompt:
      "Write a prompt to generate a comprehensive business plan for a new startup focusing on sustainable fashion, including market analysis, business model, and financial projections.",
    icon: "./prompt_template_icons/business_plan.png",
  },
  // {
  //   id: 9,
  //   title: "Literature Analysis ",
  //   prompt:
  //     "Write a prompt to generate a detailed analysis of the themes and symbols in F. Scott Fitzgerald's novel 'The Great Gatsby.'",
  //   icon: "./prompt_template_icons/tech_guide.png",
  // },
  {
    id: 10,
    title: "Health Article ",
    prompt:
      "Write a prompt to generate a detailed article about the benefits and risks of a ketogenic diet, including scientific research and expert opinions.",
    icon: "./prompt_template_icons/health_article.png",
  },
];
