import { useState } from "react";
import CategoryView from "./App/CategoryView";
import ArchivesView from "./App/ArchivesView";
import "./App.css";

function App() {
    const [view, setView] = useState("categories");

    if (view === "categories") {
        return <CategoryView setView={setView} />;
    }

    if (view === "archives") {
        return <ArchivesView setView={setView} />;
    }

    return null;
}

export default App;