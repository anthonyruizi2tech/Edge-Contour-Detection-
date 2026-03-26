import {useEffect, useState} from "react";
import {Archive} from "../archive.ts";
import {invoke} from "@tauri-apps/api/core";
import {sendSearch} from "../send_search.ts";

type Props = {
    setView: (view: string) => void;
};

function ArchivesView({ setView }: Props) {

    const [categories, setCategories] = useState<Archive[]>([]);
    const [search, setSearch] = useState("");

    async function load() {
        try {
            const result = await invoke<Archive[]>("get_shared_archives");
            setCategories(result);
        } catch (e) {}
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

                <button
                    className="btn"
                    onClick={() => setView("categories")}
                >
                    Categories
                </button>
                <button className="btn">Archives</button>


            </div>

            <div className="archives-container">
                {categories.map((cat, i) => (
                    <div className="item" key={i}>
                        <div className="item-label">{cat.title}</div>
                        <div className="item_category_label">{cat.category}</div>
                        <div className="item-timestamp-label">{cat.timestamp}</div>
                        <button className="archive-button" onClick={() => {}}>
                            Open
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ArchivesView;