import apiClient from "@/config/apiClient";

export class PersonaService {
  public async createConnection(
    userId: string,
    personaName: string
  ): Promise<() => Promise<unknown>> {
    try {
      const response = await apiClient.get(`/persona/${personaName}/${userId}`);
      return response.data;
    } catch (error) {
        throw new Error(error instanceof Error ? error.message : String(error))
    }
  }
}
