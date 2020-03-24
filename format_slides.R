library(readr)
library(stringr)

file <- "slide-construction.md"
text <- read_file(file)
#text <- "Some regular text\n\n    ## some code\n    ## [25 rows x 10 columns]\n\n Some regular text"
# replace \n-----\n with \n---\n
text <- str_replace_all(string = text, 
                pattern = "\n-----\n", 
                replacement = "\n---\n")

# fix title slide
text <- str_replace(string = text, 
                pattern = "type: slides\n", 
                replacement = "---\ntype: slides\n---\n")

# add code fence to beginning (replace "\n\n    ##" with "\n\n```out\n    ##")
text <- str_replace_all(string = text, 
            pattern = "\n\n    ##",
            replacement = "\n\n```out\n    ##")

# add code fence to end (replace "    ## .*\n\n" with "    ## *\n```\n")
# str_extract(string = text, 
#                 pattern = "(?<=    ## .*)\n\n")
# 
# str_extract(text, "(\\G(?!^)\\    ## .*\n\n)\\w+")
# 
# 
# patient <- "Name: Jane
#             Age: 25
#             Condition: OK"
# str_extract_all(patient, "(?<=Name: )")
# str_extract_all(text, "(?<=    ## .{0,100})\n\n")

text <- str_replace_all(text, "(?<=    ## .{0,100})\n\n", "\n```\n")

# remove comment blocks and indentation
text <- str_replace_all(string = text, 
                pattern = "    ## ",
                replacement = "")

write_file(text, "slide-construction-FIXED.md")