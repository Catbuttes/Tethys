from Plugins.TethysBase import TethysBase
import Tethys


def setup(bot: Tethys):
    bot.add_cog(TethysBase.TethysBase(bot))
