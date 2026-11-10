import { Link } from "react-router-dom";

function ProductCard({ item }) {

  return (
    <div className="bg-white rounded-2xl shadow-md overflow-hidden">

      {item.image_url && (
        <img
          src={item.image_url}
          alt={item.title}
          className="w-full h-48 object-cover"
        />
      )}

      <div className="p-5">

        <span className="text-sm font-medium">
          {item.type}
        </span>

        <h2 className="text-xl font-bold mt-2">
          {item.title}
        </h2>

        <p className="text-gray-600 mt-2">
          {item.description}
        </p>

        <h3 className="text-lg font-bold mt-4">
          ₹{item.price}
        </h3>

        {item.deposit > 0 && (
          <p className="text-sm">
            Deposit: ₹{item.deposit}
          </p>
        )}

        <Link
          to={`/items/${item.id}`}
          className="block mt-4 text-center bg-green-600 text-white p-3 rounded-xl"
        >
          View Details
        </Link>

      </div>

    </div>
  );
}

export default ProductCard;