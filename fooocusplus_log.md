# 0.9.4


# 0.9.1 to 0.9.3

* Resolved all security issues except those associated with GroundingDINO and RemBG,
  this involved a lot of recoding and it was the major work accomplished in these versions
* sub-optimal overrides (such as disabling Smart Memory) to support VRAM sharing have been removed
* coding has been made more streamlined and standardized
* image parameters, including the prompt, can now be changed while waiting for image generation
* the preset dropdown selector from mainline Fooocus has been restored
* work is ongoing to switch between the topbar and dropdown preset selectors
* console messages now have more clarity
* simple images with the words "Pure Fooocus" replace the distracting startup images on the main canvas
* the Fooocus metadata option has been restored and the Simple metadata option has been removed
* the mixed language preset tooltips, the Chinese only preset frame under the Settings tab, the
  Translator button and Translation Methods selector are all removed unless the command line
   argument "--language cn" (i.e. Chinese language) is present
* the "Big Model" translation method is removed since it did not work in SDXL2
* the UI Language selector is removed since it was redundant and only partially functional
* the system information displayed at the bottom of the Extras (formerly Enhanced) pane has been improved
* preliminary work on supporting Stable Diffusion 3.5 has been initiated
* the FooocusPlus version number is now tied to this log rather than being hard coded

# 0.9.0

* (2024-12-24) Forked FooocusPlus from SimpleSDXL2
* modified en.json language file to regularize capitalization, etc.
* introduced en_uk.json to support European English
* installed corrected version of watercolor_2 & mandala_art styles
* installed pony_real style in the new FooocusPlus style json

