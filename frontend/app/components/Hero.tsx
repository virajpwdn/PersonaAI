"use client";
import { FaArrowAltCircleUp } from "react-icons/fa";
import { useEffect, useRef, useState } from "react";

const Hero = () => {
  const [isMobile, setIsMobile] = useState<boolean>();
  const [transform, setTransform] = useState(0);
  const imgRef = useRef(null)

  const onMouseMoveHandler = () => {

  }

  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth < 640);

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);
  return (
    <div className="relative text-black">
      <section id="hero-section" className="">
        <p className="bg-white inline px-3 py-1 rounded-xl">
          Talk to personas and chat with them
        </p>
        <h1>Your Creative Partner, For Conversations</h1>
        <p className="max-w-lg mx-auto">
          From dynamic video generation to intelligent chat, our AI-powered
          suite helps you create compelling content and conversations. <br />
          Your all-in-one Solution for modern creation
        </p>

        <video
          src={"/gradient.mp4"}
          className="absolute bottom-0 bg-red-500 w-full rounded-tl-2xl rounded-tr-2xl h-28 sm:h-40 object-cover z-20"
          autoPlay
          loop
        ></video>
        <div
          className="absolute bottom-0 bg-gray-100 rounded-tl-2xl rounded-tr-2xl h-24! sm:h-36! box-border! z-30 left-1/2 -translate-x-1/2"
          style={{ width: "calc(100% - 1.5rem)" }}
        >
          <form action="" className="">
            <textarea
              // type="text"
              placeholder="Ask your question to Warren Buffet's Persona"
              className="mt-2 w-full px-4 outline-none resize-none"
              rows={isMobile ? 3 : 2}
            />
          </form>

          <div className="flex absolute bottom-0 w-full items-center py-2 sm:py-3 justify-end px-4">
            <button className="px-2 py-1 bg-sky-500 rounded-md">
              <FaArrowAltCircleUp className="text-xl text-white" />
            </button>
          </div>
        </div>
        <div className="rounded-lg absolute top-[52%] xl:-translate-x-1/2 translate-x-1/2 -translate-y-1/2 lg:top-[55%]">
          <img
            src="/newyork.jpg"
            alt="new york"
            className="h-80 w-72 rounded-3xl"
              style={{ clipPath: "polygon(28% 5%, 95% 5%, 72% 95%, 5% 95%)" }}
          />
        </div>
        <div
          className="absolute lg:top-[10%] xl:top-0 right-0 xl:translate-x-1/2
        -translate-x-1/2  lg:translate-y-[80%] "
        >
          <img
            src="/london.jpg"
            alt="london"
            className="h-72 w-52 rounded-lg"
          />
        </div>
      </section>
    </div>
  );
};
export default Hero;
