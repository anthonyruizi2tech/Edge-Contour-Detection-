import { useEffect, useState } from "react";
import { invoke } from "@tauri-apps/api/core";
import {Category} from "../category.ts";
import {sendSearch} from "../send_search.ts";


type Props = {
    setView: (view: string) => void;
};

function CategoryView({ setView }: Props) {
    const [categories, setCategories] = useState<Category[]>([]);
    const [search, setSearch] = useState("");

    async function load() {
        try {
            const result = await invoke<Category[]>("get_shared_categories");
            console.log("Categories:", result);
            setCategories(result);
        } catch (e) {
            console.error("Invoke failed:", e);
        }
    }

    useEffect(() => {
        load();
    }, []);



    return (
        <div>
            <div className="container">

                <input
                    className="search-bar"
                    placeholder="search"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    onKeyUp={() => {
                        sendSearch(search);
                        load();
                    }}
                />

                <button className="btn">Category</button>

                {/* Switch to Archives */}
                <button
                    className="btn"
                    onClick={() => setView("archives")}
                >
                    Archives
                </button>
            </div>

            <div className="categories-container">
                {categories.map((cat, i) => (
                    <div className="item" key={i}>
                        <div className="item-label">{cat.title}</div>
                        <button className="category-button" onClick={() => {}}>
                            Open
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default CategoryView;