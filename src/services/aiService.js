import api from "./api";

export const analyzeRequirement = async (query) => {
  try {
    const response = await api.post(
      "/api/ai/analyze",
      {
        query: query,
      }
    );

    return response.data;

  } catch (error) {
    console.error(
      "AI Analysis Error:",
      error.response?.data || error.message
    );

    throw error;
  }
};