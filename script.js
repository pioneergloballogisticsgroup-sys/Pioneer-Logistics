document.getElementById("trackBtn").addEventListener("click", function() {
  const trackingNumber = document.getElementById("trackingNumber").value.trim();
  const resultBox = document.getElementById("trackingResult");

  if (!trackingNumber) {
    resultBox.innerHTML = "<p>Please enter a tracking number.</p>";
    return;
  }

  // Show loading message
  resultBox.innerHTML = "<p>⏳ Checking...</p>";

  // Simulate a short delay before showing results (like fetching from a server)
  setTimeout(() => {
    // Mock tracking data (for now)
    const data = {
      "PG00123UK": {
        status: "In Transit",
        lastLocation: "Hamburg, Germany 🇩🇪",
        estimatedDelivery: "3–5 Business Days"
      },
      "PG00456USA": {
        status: "Delivered",
        lastLocation: "Atlanta, USA 🇺🇸",
        estimatedDelivery: "Delivered on Oct 25, 2025"
      }
    };

    const info = data[trackingNumber];
    if (info) {
      resultBox.innerHTML = `
        <div class="tracking-card">
          <p><strong>📦 Tracking Number:</strong> ${trackingNumber}</p>
          <p><strong>Status:</strong> ${info.status}</p>
          <p><strong>Last Location:</strong> ${info.lastLocation}</p>
          <p><strong>Estimated Delivery:</strong> ${info.estimatedDelivery}</p>
        </div>`;
    } else {
      resultBox.innerHTML = "<p>No record found for this tracking number.</p>";
    }
  }, 1500); // 1.5 second delay for realism
});

document.getElementById("contactForm").addEventListener("submit", async function(e) {
  e.preventDefault(); // stop the page from reloading
  const form = e.target;
  const formStatus = document.getElementById("formStatus");

  formStatus.textContent = "⏳ Sending message...";
  formStatus.style.color = "gold";

  try {
    const response = await fetch(form.action, {
      method: form.method,
      body: new FormData(form)
    });

    const result = await response.json();

    if (response.ok) {
      formStatus.textContent = "✅ Message sent successfully!";
      formStatus.style.color = "limegreen";
      form.reset();
    } else {
      formStatus.textContent = "❌ Error: " + (result.message || "Please try again.");
      formStatus.style.color = "red";
    }
  } catch (error) {
    formStatus.textContent = "⚠️ Network error. Please try again later.";
    formStatus.style.color = "red";
  }
});

// Shipment Calculator
document.getElementById("calcForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const weight = parseFloat(document.getElementById("weight").value);
  const destination = document.getElementById("destination").value;
  const result = document.getElementById("calcResult");

  if (!weight || !destination) {
    result.textContent = "❗ Please enter all fields.";
    result.style.color = "red";
    return;
  }

  result.style.color = "gray";
  result.innerHTML = "🔄 Calculating...";

  // Simulate real-world delay (like fetching from server)
  setTimeout(() => {
    const rates = {
      usa: 12,
      europe: 10,
      asia: 9,
      africa: 8
    };

    const base = rates[destination];
    const cost = (base * weight).toFixed(2);

    result.style.color = "var(--navy)";
    result.innerHTML = `💰 Estimated Shipping Cost: <strong>$${cost}</strong>`;
  }, 1200); // 1.2 seconds delay
})
// --- MOBILE MENU TOGGLE ---
document.getElementById("menu-toggle").addEventListener("click", function () {
  const navLinks = document.getElementById("nav-links");
  navLinks.classList.toggle("open");
});
// Scroll animation for panels
const panels = document.querySelectorAll('.panel');
window.addEventListener('scroll', () => {
  panels.forEach(panel => {
    const rect = panel.getBoundingClientRect();
    if (rect.top < window.innerHeight - 100) {
      panel.classList.add('visible');
    }
  });
});
