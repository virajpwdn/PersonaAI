import React from "react";

export default function AdventureStatCard({
  leftLabel = "Safari",
  pillLabel = "Adventure Travel",
  value = "35%",
  title = "Warren Buffet",
  description = "Warren Buffett is the legendary “Oracle of Omaha” and the mind behind Berkshire Hathaway—famous for calm, long-term business thinking and disciplined money habits. Chat with a Buffett-inspired mentor for clear, no-hype guidance on investing principles, research mindset, and smarter financial decisions",
  activeIndex = 1,
  totalDots = 5,
  image = "/warren.png",
}) {
  return (
    <div
      className={[
        "relative w-[340px] overflow-hidden",
        "rounded-[28px] p-5 text-white",
        "shadow-[0_18px_50px_rgba(0,0,0,0.35)]",
        //gradient background
        "bg-[radial-gradient(1200px_circle_at_15%_15%,rgba(255,147,36,0.95)_0%,rgba(255,147,36,0.55)_30%,rgba(16,16,16,0)_60%),linear-gradient(135deg,#ff7a18_0%,#7a2cff_55%,#1b1b1b_100%)]",
      ].join(" ")}
    >
      {/* soft vignette */}
      <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(800px_circle_at_30%_0%,rgba(255,255,255,0.08)_0%,rgba(0,0,0,0.55)_65%,rgba(0,0,0,0.75)_100%)]" />

      {/* Top row */}
      <div className="relative z-10 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="h-9 w-9 rounded-full bg-white/15 backdrop-blur-md flex items-center justify-center">
            <span className="text-[13px] font-semibold">{leftLabel}</span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            type="button"
            className="flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-3 py-2 text-sm font-medium backdrop-blur-md"
          >
            <span className="opacity-95">{pillLabel}</span>
            <span className="text-white/80">▾</span>
          </button>

          <button
            type="button"
            aria-label="Open"
            className="h-10 w-10 rounded-full border border-white/20 bg-white/10 backdrop-blur-md flex items-center justify-center"
          >
            <span className="text-lg leading-none">↗</span>
          </button>
        </div>
      </div>

      {/* Main stat */}
      <div className="relative z-10 mt-14">
        <div className="flex items-start gap-2">
          <div className="border-b border-zinc-400 drop-shadow-2xl">
            {/* {value} */}
            <img src={image} alt="" className="rounded-md object-cover" />
          </div>
          {/* <div className="mt-5 text-white/80 text-2xl">↗</div> */}
        </div>

        <div className="mt-5">
          <div className="text-[26px] font-semibold leading-none">{title}</div>
          <div className="mt-3 text-[13px] leading-relaxed text-white/65">
            {description}
          </div>
          <button
            type="button"
            className="
            bg-[#e0e0e0]
            rounded-[12px]
            px-10 py-5
            text-[18px]
            cursor-pointer
            transition-all duration-200 ease-in-out
            shadow-[8px_8px_16px_#bebebe,-8px_-8px_16px_#ffffff]
            shadow-[inset_6px_6px_10px_#bebebe,inset_-6px_-6px_10px_#ffffff]
            text-gray-500
            "
          >
            click here
          </button>
        </div>
      </div>

      {/* Bottom indicators */}
      {/* <div className="absolute left-0 right-0 bottom-4 z-10 flex justify-center gap-2">
        {Array.from({ length: totalDots }).map((_, i) => {
          const index = i + 1;
          const active = index === activeIndex;
          return (
            <span
              key={index}
              className={[
                "h-[6px] rounded-full transition-all",
                active ? "w-12 bg-white/90" : "w-7 bg-white/30",
              ].join(" ")}
            />
          );
        })}
      </div> */}
    </div>
  );
}
