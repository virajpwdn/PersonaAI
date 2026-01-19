"use client";
import { FaArrowAltCircleUp } from "react-icons/fa";
import { useEffect, useRef, useState } from "react";
import Navbar from "./Navbar";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";

const Hero = () => {
  const [isMobile, setIsMobile] = useState<boolean>();
  const [transform, setTransform] = useState("");
  const [transformRight, setTransformRight] = useState("");
  const imgRef = useRef<HTMLDivElement>(null);
  const imgRef2 = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLDivElement>(null);

  const onMouseMoveHandler = (e: React.MouseEvent, type: "left" | "right") => {
    if (!imgRef.current) return;

    const { top, left, width } = imgRef.current.getBoundingClientRect();
    const relativeX = (e.clientX - left) / width;
    const relativeY = (e.clientY - top) / width;

    if (type === "left") {
      const tiltX = (relativeX - 0.5) * 15;
      const tiltY = (relativeY - 0.5) * -15;

      const newTransform = `perspective(700px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(0.98, 0.98, 0.98)`;
      setTransform(newTransform);
    } else {
      const tiltX = (relativeX - 0.5) * 2;
      const tiltY = (relativeY - 0.5) * -2;

      const newTransform = `perspective(700px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(0.98, 0.98, 0.98)`;
      setTransformRight(newTransform);
    }
  };

  const onMouseLeaveHandler = () => {
    setTransform("");
    setTransformRight("");
  };

  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth < 640);

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useGSAP(() => {
    const timeline = gsap.timeline();
    timeline
      .to(videoRef.current, {
        y: 0,
        ease: "sine.inOut",
        duration: 0.6,
      })
      .to("#hero-section video", {
        opacity: 1,
        ease: "sine.inOut",
      });

    gsap.to("#text", {
      opacity: 1,
      ease: "sine.inOut",
      duration: 0.6,
    });
  });
  return (
    <div className="relative text-black max-w-5xl mx-auto">
      <Navbar />
      <section id="hero-section">
        {/* Navbar */}
        <p id="text" className="bg-white inline px-3 py-1 rounded-xl opacity-0">
          Your Creative Partner, For Conversations
        </p>
        <h1 id="text" className="opacity-0">
          Chat With the Minds You Admire
        </h1>
        <p id="text" className="max-w-lg mx-auto opacity-0">
          Persona AI lets you chat with AI personas inspired by highly
          successful individuals. Talk through your goals, decisions, and ideas
          to gain clarity, structure your plans, and move forward with
          confidence.
        </p>
        {/* Video */}
        <video
          src={"/gradient.mp4"}
          className="absolute bottom-0 bg-red-500 w-full rounded-tl-2xl rounded-tr-2xl h-28 sm:h-40 object-cover z-20 opacity-0"
          autoPlay
          loop
        ></video>
        {/* TextArea */}
        <div
          className="absolute bottom-0 bg-gray-100 rounded-tl-2xl rounded-tr-2xl h-24! sm:h-36! box-border! z-30 left-1/2 -translate-x-1/2 
          translate-y-4"
          style={{ width: "calc(100% - 1.5rem)" }}
          ref={videoRef}
        >
          <form action="">
            <textarea
              // type="text"
              placeholder="Ask your question to Warren Buffet's Persona"
              className="mt-2 w-full px-4 outline-none resize-none"
              disabled
              rows={isMobile ? 3 : 2}
            />
          </form>

          <div className="flex absolute bottom-0 w-full items-center py-2 sm:py-3 justify-end px-4">
            <button className="px-2 py-1 bg-sky-500 rounded-md">
              <FaArrowAltCircleUp className="text-xl text-white" />
            </button>
          </div>
        </div>
        {/* Images */}
        <div
          onMouseMove={(e) => {
            onMouseMoveHandler(e, "left");
          }}
          onMouseLeave={onMouseLeaveHandler}
          ref={imgRef}
          style={{ transform: transform }}
          className="rounded-lg absolute top-[52%] xl:-translate-x-1/2 translate-x-1/2 -translate-y-1/2 lg:top-[55%] transition-all ease-in duration-75 max-md:top-[65%]"
        >
          <img
            src="/elon.jpeg"
            alt="new york"
            className="h-80 w-72 rounded-3xl shadow-lg opacity-0"
            // style={{ clipPath: "polygon(28% 5%, 95% 5%, 72% 95%, 5% 95%)" }}
          />
        </div>
        <div
          className="absolute lg:top-[10%] xl:top-0 right-0 xl:translate-x-1/2
        -translate-x-1/2  lg:translate-y-[80%] transition-all ease-in duration-75 max-md:top-[40%]"
          onMouseMove={(e) => {
            onMouseMoveHandler(e, "right");
          }}
          onMouseLeave={onMouseLeaveHandler}
          ref={imgRef2}
          style={{ transform: transformRight }}
        >
          <img
            src="/warren-bg.png"
            alt="london"
            className="h-72 w-52 rounded-lg shadow-lg opacity-0 object-cover"
            // style={{ clipPath: "polygon(0 0, 80% 0, 100% 100%, 12% 100%)" }}
          />
        </div>
      </section>
    </div>
  );
};
export default Hero;
