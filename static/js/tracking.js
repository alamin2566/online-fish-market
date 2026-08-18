/**
 * tracking.js — Centralized e-commerce event tracker
 *
 * HOW IT WORKS:
 * 1. Load this file ONCE in base.html (after MyAnalytics.init() has run).
 * 2. On any page where you want to track an event, add ONE small
 *    <script> block that sets `window.pageTrackingData` BEFORE this
 *    file loads. This file reads it and fires the correct event
 *    automatically. You never call MyAnalytics.track() yourself.
 *
 * Pages that don't set window.pageTrackingData simply do nothing —
 * safe to include everywhere.
 */

(function () {
  function safeTrack(eventName, properties) {
    if (typeof MyAnalytics === "undefined" || !MyAnalytics.track) {
      console.warn("[tracking.js] MyAnalytics not loaded yet, skipping:", eventName);
      return;
    }
    MyAnalytics.track(eventName, properties);
  }

  function normalizeItems(items) {
    // Accepts an array of {id, name, price, quantity} and converts to
    // the {productId, productName, price, quantity} shape the backend expects.
    return (items || []).map(function (i) {
      return {
        productId: i.productId || i.id,
        productName: i.productName || i.name,
        price: Number(i.price),
        quantity: Number(i.quantity || 1),
      };
    });
  }

  function calcValue(items) {
    return items.reduce(function (sum, i) {
      return sum + i.price * i.quantity;
    }, 0);
  }

  function run() {
    var data = window.pageTrackingData;
    if (!data || !data.type) return; // nothing to track on this page

    switch (data.type) {
      case "product_view": {
        var p = data.product;
        safeTrack("product_view", {
          productId: p.id,
          productName: p.name,
          price: Number(p.price),
        });
        break;
      }

      case "add_to_cart": {
        var p2 = data.product;
        safeTrack("add_to_cart", {
          productId: p2.id,
          productName: p2.name,
          price: Number(p2.price),
          quantity: Number(data.quantity || 1),
        });
        break;
      }

      case "view_cart": {
        var items = normalizeItems(data.items);
        safeTrack("view_cart", {
          items: items,
          value: calcValue(items),
        });
        break;
      }

      case "begin_checkout": {
        var items2 = normalizeItems(data.items);
        safeTrack("begin_checkout", {
          items: items2,
          value: calcValue(items2),
        });
        break;
      }

      case "purchase": {
        var items3 = normalizeItems(data.items);
        safeTrack("purchase", {
          orderId: data.orderId,
          currency: data.currency || "BDT",
          value: data.value !== undefined ? Number(data.value) : calcValue(items3),
          items: items3,
        });
        break;
      }

      default:
        console.warn("[tracking.js] Unknown tracking type:", data.type);
    }
  }

  // Also expose manual functions in case you ever need to fire an event
  // from a button click (e.g. Add to Cart) instead of on page load.
  window.Tracker = {
    viewProduct: function (product) {
      safeTrack("product_view", {
        productId: product.id,
        productName: product.name,
        price: Number(product.price),
      });
    },
    addToCart: function (product, quantity) {
      safeTrack("add_to_cart", {
        productId: product.id,
        productName: product.name,
        price: Number(product.price),
        quantity: Number(quantity || 1),
      });
    },
    viewCart: function (items) {
      var norm = normalizeItems(items);
      safeTrack("view_cart", { items: norm, value: calcValue(norm) });
    },
    beginCheckout: function (items) {
      var norm = normalizeItems(items);
      safeTrack("begin_checkout", { items: norm, value: calcValue(norm) });
    },
    purchase: function (orderId, items, currency) {
      var norm = normalizeItems(items);
      safeTrack("purchase", {
        orderId: orderId,
        currency: currency || "BDT",
        value: calcValue(norm),
        items: norm,
      });
    },
  };

  // Auto-fire on page load if pageTrackingData was set before this script ran.
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
