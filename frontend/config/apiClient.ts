import axios from "axios";
import { baseUrl } from "@/utils/constants";

const apiClient = axios.create({
  baseURL: baseUrl,
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true
});

export default apiClient