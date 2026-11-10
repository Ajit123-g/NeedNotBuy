function ProductCard({ item, onViewDetails }) {

  return (
    <div className="bg-white rounded-2xl shadow-sm
      border border-gray-100 overflow-hidden
      hover:shadow-lg transition">

      <img
        src={item.image_url || "/placeholder.png"}
        alt={item.title}
        className="w-full h-48 object-cover"
      />

      <div className="p-5">

        <span className="text-sm text-green-700
          bg-green-50 px-3 py-1 rounded-full">
          {item.type}
        </span>

        <h2 className="font-bold text-lg mt-3">
          {item.title}
        </h2>

        <p className="text-gray-500 text-sm mt-2">
          {item.description}
        </p>

        <p className="font-bold text-xl mt-4">
          ₹{item.price}
        </p>

        <button
          onClick={() => onViewDetails(item.id)}
          className="w-full mt-4 bg-green-600
            text-white p-3 rounded-xl"
        >
          View Details
        </button>

      </div>

    </div>
  );
}

export default ProductCard;