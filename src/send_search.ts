import {invoke} from "@tauri-apps/api/core";

export async function sendSearch(search: string) {
    try {
        await invoke("update_search_filter", { input: search });
    } catch (e) {
        console.error("Failed to send search:", e);
    }
}