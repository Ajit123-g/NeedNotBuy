import { useEffect, useState } from "react";
import { getRecommendations } from "../services/itemService";
import ProductCard from "../components/ProductCard";

function Results() {

  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {

    const fetchItems = async () => {

      try {

        setLoading(true);

        const data = await getRecommendations("projector");

        setItems(data);

      } catch (err) {

        console.error(err);

        setError("Unable to load recommendations.");

      } finally {

        setLoading(false);

      }

    };

    fetchItems();

  }, []);

  if (loading) {
    return <h2>Finding smarter options...</h2>;
  }

  if (error) {
    return <h2>{error}</h2>;
  }

  return (
    <div>

      <h1>Smarter Options</h1>

      <div>
        {items.map((item) => (
          <ProductCard
            key={item.id}
            item={item}
          />
        ))}
      </div>

    </div>
  );
}

export default Results;