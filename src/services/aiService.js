import api from "./api";

export const analyzeRequirement = async (query) => {
  const response = await api.post(
    "/api/ai/analyze",
    {
      query: query,
    }
  );

  return response.data;
};