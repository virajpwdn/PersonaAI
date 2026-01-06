"use client";
import React, { useRef } from "react";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";

export default function AdventureStatCard({
  leftLabel = "Safari",
  pillLabel = "Adventure Travel",
  value = "35%",
  title = "Warren Buffet",
  description = "Warren Buffett is the legendary 'Oracle of Omaha' and the mind behind Berkshire Hathaway—famous for calm, long-term business thinking and disciplined money habits. Chat with a Buffett-inspired mentor for clear, no-hype guidance on investing principles, research mindset, and smarter financial decisions",
  activeIndex = 1,
  totalDots = 5,
  image = "/warren.png",
}) {
  const cardRef = useRef<HTMLDivElement>(null);

  // useGSAP(() => {
  //   gsap.from(".card-container", {
  //     scale: 0,
  //     opacity: 0,
  //     duration: 0.6,
  //     ease: "back.out",
  //   });
  // });

  const handleMouseEnter = () => {
    gsap.to(cardRef.current, {
      backgroundImage:
        "radial-gradient(1200px circle at 85% 85%, rgba(123, 44, 255, 0.95) 0%, rgba(123, 44, 255, 0.55) 30%, rgba(16, 16, 16, 0) 60%), linear-gradient(135deg, #7a2cff 0%, #ff7a18 55%, #1b1b1b 100%)",
      duration: 0.8,
      ease: "power2.inOut",
    });
  };

  const handleMouseLeave = () => {
    gsap.to(cardRef.current, {
      backgroundImage:
        "radial-gradient(1200px circle at 15% 15%, rgba(255, 147, 36, 0.95) 0%, rgba(255, 147, 36, 0.55) 30%, rgba(16, 16, 16, 0) 60%), linear-gradient(135deg, #ff7a18 0%, #7a2cff 55%, #1b1b1b 100%)",
      duration: 0.8,
      ease: "power2.inOut",
    });
  };

  const mouseMoveHandler = (e: React.MouseEvent) => {
    if (!cardRef.current) return;
    const { clientX, clientY } = e;

    const rect = cardRef.current?.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const xPercent = (x / rect.width) * 100;
    const yPercent = (y / rect.height) * 100;

    const clampedX = Math.max(10, Math.min(90, xPercent));
    const clampedY = Math.max(10, Math.min(90, yPercent));

    gsap.to(cardRef.current, {
      "--gradient-pos-x": `${clampedX}%`,
      "--gradient-pos-y": `${clampedY}%`,
      ease: "power1.out",
      overwrite: "auto",
    });
  };

  return (
    <div
      ref={cardRef}
      className="card-container"
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      onMouseMove={mouseMoveHandler}
    >
      {/* Soft vignette */}
      <div className="vignette-overlay" />

      {/* Top row */}
      <div className="relative z-10 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="badge-circle">
            <span className="text-[13px] font-semibold">{leftLabel}</span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button type="button" className="glass-button">
            <span className="opacity-95">{pillLabel}</span>
            <span className="text-white/80">▾</span>
          </button>
          <button type="button" aria-label="Open" className="icon-button">
            <span className="text-lg leading-none">↗</span>
          </button>
        </div>
      </div>

      {/* Main stat */}
      <div className="relative z-10 mt-14">
        <div className="flex items-start gap-2">
          <div className="border-b border-zinc-400 drop-shadow-2xl">
            <img src={image} alt="main" className="rounded-md object-cover" />
          </div>
        </div>

        <div className="mt-5">
          <div className="text-[26px] font-semibold leading-none">{title}</div>
          <div className="mt-3 text-[13px] leading-relaxed text-white/65">
            {description}
          </div>
          <button type="button" className="neumorphic-btn mt-4">
            click here
          </button>
        </div>
      </div>
    </div>
  );
}
