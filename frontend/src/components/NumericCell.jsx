import { useState, useRef } from "react";

/**
 * NumericCell - مثل اکسل:
 * - موقع نمایش: رند، با جداکننده هزارگان، بدون اعشار
 * - موقع کلیک: عدد خام قابل ویرایش
 * - با Tab و Enter از سلول خارج میشه
 */
export default function NumericCell({
  value,
  onChange,
  disabled = false,
  className = "",
  style = {},
}) {
  const [editing, setEditing] = useState(false);
  const inputRef = useRef(null);

  // فرمت نمایش: رند + جداکننده هزارگان
  function formatDisplay(val) {
    if (val === null || val === undefined || val === "") return "";
    const n = parseFloat(val);
    if (isNaN(n)) return val;
    // رند به نزدیکترین عدد صحیح
    return Math.round(n).toLocaleString("en-US");
  }

  function handleClick() {
    if (disabled) return;
    setEditing(true);
    setTimeout(() => {
      if (inputRef.current) {
        inputRef.current.focus();
        inputRef.current.select();
      }
    }, 0);
  }

  function handleBlur() {
    setEditing(false);
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" || e.key === "Tab") {
      setEditing(false);
    }
    if (e.key === "e" || e.key === "E") {
      e.preventDefault();
    }
  }

  const baseStyle = {
    textAlign: "left",
    direction: "ltr",
    minWidth: "100px",
    cursor: disabled ? "default" : "text",
    ...style,
  };

  if (editing && !disabled) {
    return (
      <input
        ref={inputRef}
        className={`form-control num-input ${className}`}
        type="number"
        step="any"
        value={value ?? ""}
        onChange={(e) => onChange(e.target.value)}
        onBlur={handleBlur}
        onKeyDown={handleKeyDown}
        style={baseStyle}
      />
    );
  }

  return (
    <div
      className={`form-control num-input num-display ${className} ${disabled ? "disabled-cell" : ""}`}
      onClick={handleClick}
      style={{
        ...baseStyle,
        backgroundColor: disabled ? "#f8f9fa" : "#fff",
        color: disabled ? "#6c757d" : "inherit",
        userSelect: "none",
      }}
    >
      {formatDisplay(value)}
    </div>
  );
}
