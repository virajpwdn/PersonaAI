"use client";
import Card from "../components/Card";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { useRef } from "react";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);
const Page = () => {
  const name = "Warren Buffet";
  const description =
    "Billionare Investor, Giving advice about how to invest money, how to manage wealth, business advice. Warren is a calm person and he has to many friends in business world.";
  const src = "/warren-bg.png";
  const imgAlt = "Warren Buffet Persona";

  const imgRef = useRef<HTMLDivElement[]>([]);
  const nextRef = useRef<HTMLDivElement[]>([]);

  useGSAP(() => {
    gsap.set(imgRef.current, { visibility: "visible" });
    gsap.to(imgRef.current, {
      opacity: 1,
      y: -20,
      stagger: 0.5,
      ease: "sine.inOut",
    });
  }, []);

  useGSAP(() => {
    const timeline = gsap.timeline({
      scrollTrigger: {
        trigger: nextRef.current,
        start: "top center",
        end: "bottom bottom",
        scrub: 3,
        // markers: true,
      },
    });

    timeline.to(nextRef.current, {
      opacity: 1,
      y: -10,
      stagger: 0.5,
      // duration: 1,
      ease: "sine.inOut",
    });
  }, []);

  return (
    <>
      <section className="h-dvh w-screen mt-30">
        <div className="container mx-auto">
          <div className="flex flex-col md:flex-row items-center justify-center gap-5">
            {[0, 1].map((index) => (
              <Card
                key={index}
                ref={(el) => {
                  if (el) imgRef.current[index] = el;
                }}
                name={name}
                description={description}
                src={src}
                imgAlt={imgAlt}
              />
            ))}
          </div>

          {/* Bottom Cards */}
          <div className="flex flex-col md:flex-row items-center justify-center gap-5 py-20">
            {[0, 1].map((idx) => (
              <Card
                key={idx}
                ref={(el) => {
                  if (el) nextRef.current[idx] = el;
                }}
                name={name}
                description={description}
                src={src}
                imgAlt={imgAlt}
              />
            ))}
          </div>
        </div>
      </section>
    </>
  );
};
export default Page;
