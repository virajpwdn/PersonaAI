import { forwardRef } from "react";
import {
  FaArrowCircleLeft,
  FaArrowCircleRight,
  FaArrowCircleUp,
} from "react-icons/fa";
import { useRouter } from "next/navigation";

interface CardProps {
  name: string;
  src: string;
  description: string;
  imgAlt: string;
  link: string;
}

const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ name, src, description, imgAlt, link }, ref) => {
    const router = useRouter()
    return (
      <div
        ref={ref}
        className="max-w-[350px] bg-white rounded-4xl p-5 opacity-0 shadow-lg"
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
          <button onClick={() => {
            router.push(`/persona/${link}`)
          }} className="bg-sky-500 px-8 font-bold py-3 rounded-xl cursor-pointer">
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
