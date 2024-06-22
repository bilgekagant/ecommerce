import { get, post } from "./request";
const apiUrl = "https://localhost:7153/api";
export const getColors = () => get(apiUrl + "/colors/getall");

export const postColor = (color) => post(apiUrl + "/colors/add", color);

export const updateColor = (data) => post(apiUrl + "/colors/update", data);

export const deleteColor = (colorId) =>
  get(apiUrl + "/colors/delete?colorId=" + colorId);
