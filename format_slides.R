"Post-processing of R Markdown generated markdown file slides for Ines Montani open course framework.

Usage: format_slides.R --input=<input> [--output=<output>]
  
Options:
  --input=<input>       Path (including filename) to input markdown file to be pre-processed
  [--output=<output>]   Optional path (including filename) to output file (if not used then input path/filename is used)
" -> doc

library(docopt)
library(readr)
library(stringr)

opt <- docopt(doc)

main <- function(input) {

  text <- read_file(input)

  # replace \n-----\n with \n---\n to denote slide breaks
  text <- str_replace_all(string = text, 
                          pattern = "\n-----\n", 
                          replacement = "\n---\n")
  
  # fix title slide
  text <- str_replace(string = text, 
                      pattern = "type: slides\n", 
                      replacement = "---\ntype: slides\n---\n")
  
  # add backtick code fence and out to beginning of output code chunks
  text <- str_replace_all(string = text, 
                          pattern = "\n\n    ##",
                          replacement = "\n\n```out\n    ##")
  
  # add backtick code fence to end of output code chunks
  text <- str_replace_all(text, "(?<=    ## .{0,300})\n\n", "\n```\n\n")
  
  # remove comment blocks and indentation from output code chunks
  text <- str_replace_all(string = text, 
                          pattern = "    ## ",
                          replacement = "")
  
  if (!is.null(opt[["--output"]])) {
    write_file(text, opt[["--output"]])
  } else {
    write_file(text, input)
  }
}

main(opt[["--input"]])