return {
	{
		"nvim-treesitter/nvim-treesitter",
		init = function()
			vim.opt.runtimepath:prepend(vim.fn.stdpath("data") .. "/site")
		end,
		opts = {
			ensure_installed = {
				"bash",
				"json",
				"lua",
				"markdown",
				"markdown_inline",
				"toml",
				"yaml",
			},
		},
	},
}
