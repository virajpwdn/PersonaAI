import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);
const Navbar = () => {
  //   useGSAP(() => {
  //     // const timeline = gsap.timeline({
  //     //     scrollTrigger: {
  //     //         trigger: "#navbar-section",
  //     //         start: "top top",
  //     //         end: "top top",
  //     //         markers: true,
  //     //         scrub: 1,
  //     //         pin: true
  //     //     }
  //     // })

  //     // timeline.to("img", {
  //     //     opacity: 0,
  //     //     x: 10,
  //     //     ease: "sine.inOut"
  //     // })
  //     const timeline = gsap.timeline();
  //     // gsap.set(["img", "h3", ".nav-links", ".nav-buttons"], {
  //     //   opacity: 0,
  //     //   x: -20,
  //     // });

  //     // Animate all at once with stagger
  //     // timeline.to(["#navbar-section", "img", "nav-links", "li", ".nav-buttons"], {
  //     //   opacity: 1,
  //     //   x: 0,
  //     //   y:0,
  //     //   duration: 0.4,
  //     //   ease: "sine.inOut",
  //     //   stagger: 0.2, // 0.2s delay between each element
  //     // });
  //     timeline.to("#navbar-section img", {
  //       opacity: 1,
  //       x: 0,
  //       duration: 0.2,
  //       ease: "sine.inOut",
  //     });
  //   });

  useGSAP(() => {
    const timeline = gsap.timeline();

    // Start with elements invisible
    gsap.set(
      [
        "img",
        "h3",
        "#nav-links",
        "#nav-buttons",
        "#navbar-section",
        "#links-bg",
      ],
      {
        opacity: 0,
      }
    );

    // Animate in sequence
    timeline
      .to("#navbar-section", {
        opacity: 1,
        y: 0,
        x: 0,
        duration: 0.6,
        ease: "sine.inOut",
      })
      .to("img", {
        opacity: 1,
        x: 0,
        duration: 0.6,
        ease: "sine.inOut",
      })
      .to(
        "#navbar-section h3",
        {
          opacity: 1,
          x: 0,
          duration: 0.6,
          ease: "sine.inOut",
        },
        "-=0.3"
      )
      .to(
        "#links-bg",
        {
          opacity: 1,
          duration: 0.3,
          ease: "sine.inOut",
        },
        "-=0.3"
      )
      .to("#nav-links", {
        opacity: 1,
        scale: 1,
        duration: 0.3,
        ease: "sine.inOut",
        stagger: 1,
      })
      .to(
        "#nav-buttons",
        {
          opacity: 1,
          duration: 0.3,
          delay: 0.2,
          ease: "sine.inOut",
          stagger: 1,
        },
        "-=0.3"
      );
  }, []);
  return (
    <div
      id="navbar-section"
      className="flex-between z-100 -translate-y-2 opacity-0"
    >
      <div className="flex items-center gap-4">
        <img
          src="/logo-1.png"
          className="h-14 w-14 rounded-full -translate-x-2 object-cover scale-150"
        />
        <h3 className="text-lg font-black uppercase">Persona AI</h3>
      </div>
      <div
        id="links-bg"
        className="bg-gray-100 px-10 py-2 rounded-full hidden md:block"
      >
        <ul
          id="nav-links"
          className="flex-center gap-4 font-semibold scale-110"
        >
          <li>Features</li>
          <li>Pricing</li>
          <li>Blogs</li>
        </ul>
      </div>
      <div id="nav-buttons" className="flex gap-4 font-semibold">
        <button className="secondary-button cursor-pointer">Login</button>
        <button className="primary-button bg-black cursor-pointer text-white">
          Sign up
        </button>
      </div>
    </div>
  );
};
export default Navbar;
