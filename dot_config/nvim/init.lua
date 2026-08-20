local site = vim.fn.stdpath("data") .. "/site"
vim.opt.runtimepath:prepend(site)
vim.opt.packpath:prepend(site)

require("config.lazy")
