import api from "./api";

export const uploadResume = async (
  formData: FormData
) => {
  const response = await api.post(
    "/api/v1/resume/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};