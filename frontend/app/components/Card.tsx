import { forwardRef } from "react";
import {
  FaArrowCircleLeft,
  FaArrowCircleRight,
  FaArrowCircleUp,
} from "react-icons/fa";

interface CardProps {
  name: string;
  src: string;
  description: string;
  imgAlt: string;
}

const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ name, src, description, imgAlt }, ref) => {
    return (
      <div
        ref={ref}
        className="max-w-[350px] bg-[#fff] rounded-4xl p-5 opacity-0"
      >
        <div className="relative">
          <img src={src} alt={imgAlt} className="rounded-3xl shadow-xl" />
        </div>
        <div className="mt-5 px-4">
          <h2 className="font-bold text-2xl">{name}</h2>
          <p className="leading-5">{description}</p>
        </div>
        {/* chat button */}
        <div className="mt-5 flex justify-between items-center px-4">
          <button className="bg-sky-500 px-8 font-bold py-3 rounded-xl">
            Chat
          </button>
          <FaArrowCircleRight size={28} />
        </div>
      </div>
    );
  }
);

Card.displayName = "Card";

export default Card;
