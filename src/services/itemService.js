import { Search } from "lucide-react";
import api from "./api";

export const getItems = async (params = {}) => {

  const response = await api.get("/api/items", {
    params,
  });

  return response.data;
};

export const getItemById = async (id) => {

  const response = await api.get(`/api/items/${id}`);

  return response.data;
};


export const getRecommendations=async (item)=>{
  const response=await api.get("/api/items",
    {
      params:{
        search: item,
      },
    });
    return response.data;
  };