"use client";
import Card from "../components/Card";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { useEffect, useRef } from "react";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { persona } from "@/utils/constants";
import { useRouter } from "next/navigation";

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

  useEffect(() => {
    // For creating connection
  }, []);

  return (
    <>
      <section className="h-dvh container mx-auto mt-30">
        <div className="">
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
          <div className="grid grid-cols-2 justify-center mx-auto w-fit gap-5 gap-y-20 py-20">
            {persona.map((item, idx) => (
              <Card
                key={item.uni}
                ref={(el) => {
                  if (el) nextRef.current[idx] = el;
                }}
                name={item.name}
                description={description}
                src={src}
                imgAlt={imgAlt}
                link={`${item.uni}/connectionid`}
              />
            ))}
          </div>
        </div>
      </section>
    </>
  );
};
export default Page;
