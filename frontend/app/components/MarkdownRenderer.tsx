import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function MarkdownRenderer({ mdContent }) {
  // Backend sends data in md formart, so adding custom styling to every html tag
  return (
    <div className="max-w-4xl mx-auto p-6 bg-transparent">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          // Headings
          h1: ({ node, ...props }) => (
            <h1
              className="text-4xl font-bold mt-8 mb-4 text-black"
              {...props}
            />
          ),
          h2: ({ node, ...props }) => (
            <h2
              className="text-3xl font-bold mt-7 mb-3 text-black"
              {...props}
            />
          ),
          h3: ({ node, ...props }) => (
            <h3
              className="text-2xl font-bold mt-6 mb-3 text-black"
              {...props}
            />
          ),
          h4: ({ node, ...props }) => (
            <h4 className="text-xl font-bold mt-5 mb-2 text-black" {...props} />
          ),

          // Paragraphs
          p: ({ node, ...props }) => (
            <p className="text-base leading-7 mb-4 text-gray-800" {...props} />
          ),

          // Lists
          ul: ({ node, ...props }) => (
            <ul
              className="list-disc list-inside mb-4 ml-4 text-gray-800"
              {...props}
            />
          ),
          ol: ({ node, ...props }) => (
            <ol
              className="list-decimal list-inside mb-4 ml-4 text-gray-800"
              {...props}
            />
          ),
          li: ({ node, ...props }) => (
            <li className="mb-2 leading-7" {...props} />
          ),

          // Code blocks
          code: ({ node, inline, ...props }) => {
            if (inline) {
              return (
                <code
                  className="bg-gray-200 px-2 py-1 rounded text-sm font-mono text-black"
                  {...props}
                />
              );
            }
            return (
              <code
                className="block bg-gray-200 p-4 rounded-lg mb-4 overflow-x-auto text-sm font-mono text-black"
                {...props}
              />
            );
          },

          // Pre (code block wrapper)
          pre: ({ node, ...props }) => (
            <pre
              className="bg-gray-200 p-4 rounded-lg mb-4 overflow-x-auto"
              {...props}
            />
          ),

          // Tables
          table: ({ node, ...props }) => (
            <table
              className="w-full border-collapse border border-gray-300 mb-4"
              {...props}
            />
          ),
          thead: ({ node, ...props }) => (
            <thead className="bg-gray-100" {...props} />
          ),
          th: ({ node, ...props }) => (
            <th
              className="border border-gray-300 px-4 py-3 text-left font-semibold text-black"
              {...props}
            />
          ),
          td: ({ node, ...props }) => (
            <td
              className="border border-gray-300 px-4 py-3 text-gray-800"
              {...props}
            />
          ),

          // Blockquote
          blockquote: ({ node, ...props }) => (
            <blockquote
              className="border-l-4 border-gray-400 pl-4 py-2 mb-4 italic text-gray-700 bg-gray-50"
              {...props}
            />
          ),

          // Horizontal rule
          hr: ({ node, ...props }) => (
            <hr className="my-6 border-gray-300" {...props} />
          ),

          // Links
          a: ({ node, ...props }) => (
            <a className="text-blue-600 hover:underline" {...props} />
          ),

          // Strong and emphasis
          strong: ({ node, ...props }) => (
            <strong className="font-bold text-black" {...props} />
          ),
          em: ({ node, ...props }) => (
            <em className="italic text-gray-700" {...props} />
          ),
        }}
      >
        {mdContent}
      </ReactMarkdown>
    </div>
  );
}
